import cn from 'classnames';
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAppSelector } from '../../app/hooks';
import { userSelector } from '../../app/selectors/userSelector';
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
  const [starsValue, setStarsValue] = useState('')
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

    if (btnType === 'unavailable') {
      console.log(unavailableValue)
      localStorage.setItem('unavailable_value', '')
      setUnavailableValue('')
    } else {
      console.log(reviewValue, starsValue)
      localStorage.setItem('stars_value', '')
      localStorage.setItem('review_value', '')
      setStarsValue('')
      setReviewValue('')
    }
  }

  function onStarsChange(event: React.ChangeEvent<HTMLInputElement>) {
    localStorage.setItem('stars_value', event.target.value)
    setStarsValue(event.target.value)
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
            placeholder='Сообщите о недоступности...'
            maxLength={255}
            onChange={onUnavailableChange}
          />
        </div>
        <Button 
          btnType='red'
          onClick={() => btnsClickHandler('unavailable')}
          disabled={unavailableValue.length < 1}
        >
          {isAuth 
            ? 'Сообщить о недоступности' : 'Авторизоваться и сообщить о недоступности'
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