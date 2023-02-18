import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAppSelector } from '../../app/hooks';
import { isAuthSelector } from '../../app/selectors/isAuthSelector';
import { AUTH_ROUTE, SOURCES_ROUTE } from '../../utils/constants';
import Card from '../Card/Card';
import Button from '../UI/Button/Button';
import TextArea from '../UI/TextArea/TextArea';
import styles from './ReviewCard.module.scss'
import { ReviewCardPropsType } from './ReviewCardTypes';

const ReviewCard = ({sourceId, ...props}: ReviewCardPropsType) => {
  const navigate = useNavigate()
  const isAuth = useAppSelector(isAuthSelector)
  const [reviewValue, setReviewValue] = useState('')
  const [unavailableValue, setUnavailableValue] = useState('')

  function btnsClickHandler(btnType: string) {
    if (!isAuth) {
      navigate(AUTH_ROUTE + `?next_page=${SOURCES_ROUTE + '/' + sourceId}`)
    }

    console.log(btnType === 'review' ? reviewValue : unavailableValue)
  }

  function onReviewChange(event: React.ChangeEvent<HTMLTextAreaElement>) {
    setReviewValue(event.target.value)
  }

  function onUnavailableChange(event: React.ChangeEvent<HTMLTextAreaElement>) {
    setUnavailableValue(event.target.value)
  }

  return (
    <Card 
      title='Оставьте отзыв или сообщите о недоступности ресурса'
      description='Сообщайте о недоступности ресурсов и оставляйте отзывы, пополняя общую базу данных'
      {...props}
    >
      <>
        {isAuth &&
          <div className={styles.textarea_wrapper}>
            <TextArea
              name='reviews'
              placeholder='Сообщите о недоступности...'
              maxLength={255}
              onChange={onUnavailableChange}
              disabled={!isAuth}
            />
          </div>
        }
        <Button 
          btnType='red'
          onClick={() => btnsClickHandler('unavailable')}
          disabled={unavailableValue.length < 1 && isAuth}
        >
          {isAuth 
            ? 'Сообщить о недоступности' : 'Авторизоваться и сообщить о недоступности'
          }
        </Button>
        {isAuth &&
          <div className={styles.textarea_wrapper}>
            <TextArea
              name='reviews'
              placeholder='Оставьте отзыв...'
              maxLength={255}
              onChange={onReviewChange}
            />
          </div>
        }
        <Button 
          btnType='fill_purple'
          onClick={() => btnsClickHandler('review')}
          disabled={reviewValue.length < 1 && isAuth}
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