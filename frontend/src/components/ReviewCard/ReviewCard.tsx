import cn from 'classnames';
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import { useAppSelector } from '../../app/hooks';
import { userSelector } from '../../app/selectors/userSelector';
import { usePostReportMutation, usePostReviewMutation } from '../../services/apiService/apiService';
import { AUTH_ROUTE, SOURCES_ROUTE } from '../../utils/constants';
import Card from '../Card/Card';
import Button from '../UI/Button/Button';
import TextArea from '../UI/TextArea/TextArea';
import styles from './ReviewCard.module.scss';
import { ReviewCardPropsType } from './ReviewCardTypes';


const ReviewCard = ({sourceUuid, ...props}: ReviewCardPropsType) => {
  const navigate = useNavigate()
  const {isAuth} = useAppSelector(userSelector)
  const [reviewValue, setReviewValue] = useState('')
  const [isSayUnavailable, setIsSayUnavailable] = useState(false)
  const [starsValue, setStarsValue] = useState('')
  const [postReport] = usePostReportMutation()
  const [postReview] = usePostReviewMutation()
  const [unavailableValue, setUnavailableValue] = useState('')
  
  useEffect(() => {
    setUnavailableValue(localStorage.getItem('unavailable_value') || '')
    setReviewValue(localStorage.getItem('review_value') || '')
    setStarsValue(localStorage.getItem('stars_value') || '')
  }, [isAuth])

  function btnsClickHandler(btnType: string) {
    if (!isAuth) {
      navigate(AUTH_ROUTE + `?next_page=${SOURCES_ROUTE + '/' + sourceUuid}`)
      return
    }

    if (btnType !== 'review') {
      console.log({
        status: btnType === 'unavailable' ? 'critical' : 'OK',
        is_moderated: false, 
        resource_uuid: sourceUuid,
        text: btnType === 'unavailable' ? unavailableValue : ''
    })
      postReport({
        status: btnType === 'unavailable' ? 'critical' : 'OK',
        is_moderated: false, 
        resource_uuid: sourceUuid,
        text: btnType === 'unavailable' ? unavailableValue : ''
    }).then(value => {
        if ('error' in value) {
          toast("Ошибка при отправлении сообщения")
          return
        }

        setIsSayUnavailable(true)
        toast("Сообщение успешно отправлено")

        if (btnType === 'unavailable') {
          localStorage.setItem('unavailable_value', '')
          setUnavailableValue('')
        } 
      })
    } else {
      postReview({
        text: reviewValue,
        stars: +starsValue,
        resource_uuid: sourceUuid
      }).then(value => {
        if ('error' in value) {
          toast('Ошибка при отправлении отзыва')
          return
        }

        localStorage.setItem('stars_value', '')
        localStorage.setItem('review_value', '')
        setStarsValue('')
        setReviewValue('')

        toast('Отзыв успешно отправлен!')
      })
    }
  }

  function onStarsChange(event: React.ChangeEvent<HTMLInputElement>) {
    const value = event.target.value
    if (value !== '' && (value.length > 1 || +value > 5 || +value < 1)) {
      return
    }
    localStorage.setItem('stars_value', value)
    setStarsValue(value)
  }

  function onReviewChange(event: React.ChangeEvent<HTMLTextAreaElement>) {
    localStorage.setItem('review_value', event.target.value)
    setReviewValue(event.target.value)
  }

  function onUnavailableChange(event: React.ChangeEvent<HTMLTextAreaElement>) {
    localStorage.setItem('unavailable_value', event.target.value)
    setUnavailableValue(event.target.value)
  }

  return (
    <Card 
      title='Оставьте отзыв или сообщите о недоступности ресурса'
      description='Сообщайте о недоступности ресурсов и оставляйте отзывы, пополняя общую базу данных'
      {...props}
    >
      <>
        <div className={styles.textarea_wrapper}>
          <TextArea
            name='unavailable'
            value={unavailableValue}
            placeholder='Опишите проблему...'
            maxLength={255}
            onChange={onUnavailableChange}
          />
        </div>
        <Button 
          btnType='red'
          onClick={() => btnsClickHandler('unavailable')}
          disabled={isSayUnavailable || unavailableValue.length < 1}
        >
          {isAuth 
            ? 'Сообщить о недоступности' : 'Авторизоваться и сообщить о недоступности'
          }
        </Button>
        <Button 
          btnType='green'
          onClick={() => btnsClickHandler('available')}
          disabled={isSayUnavailable}
        >
          {isAuth 
            ? 'Все работает' : 'Авторизоваться и сообщить о недоступности'
          }
        </Button>
        <div className={styles.textarea_wrapper}>
          <TextArea
            name='reviews'
            value={reviewValue}
            placeholder='Оставьте отзыв...'
            maxLength={255}
            onChange={onReviewChange}
          />
        </div>
        <div className={cn(styles.textarea_wrapper, styles.stars)}>
          <input
            onChange={onStarsChange}
            type="number"
            value={starsValue}
            className={styles.number_input}
            placeholder='1'
            min='1'
            max='5'
          />
        </div>
        <Button 
          btnType='fill_purple'
          onClick={() => btnsClickHandler('review')}
          disabled={
            starsValue.length > 1 || +starsValue > 5 || +starsValue < 1
          }
        >
          {isAuth 
            ? 'Оставить отзыв' : 'Авторизоваться и оставить отзыв'
          }
        </Button>
      </>
    </Card>
  );
};

export default ReviewCard;