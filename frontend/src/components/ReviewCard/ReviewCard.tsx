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

  function leaveReviewClickHandler() {
    if (!isAuth) {
      navigate(AUTH_ROUTE + `?next_page=${SOURCES_ROUTE + '/' + sourceId}`)
    }

    console.log(reviewValue)
  }

  function onReviewChange(event: React.ChangeEvent<HTMLTextAreaElement>) {
    setReviewValue(event.target.value)
  }

  return (
    <Card title='Оставьте отзыв' {...props}>
      <div className={styles.wrapper}>
        <span className={styles.description}>
          Сообщайте о недоступности ресурсов и оставляйте отзывы, пополняя общую базу данных
        </span>
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
          onClick={leaveReviewClickHandler}
          disabled={reviewValue.length < 1 && isAuth}
        >
          {isAuth 
            ? 'Оставить отзыв' : 'Авторизоваться и оставить отзыв'
          }
        </Button>
      </div>
    </Card>
  );
};

export default ReviewCard;