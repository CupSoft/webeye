import { useGetAllReviewsQuery } from '../../services/apiService/apiService';
import { ReviewGetTypes } from '../../services/apiService/apiServiceTypes';
import Card from '../Card/Card';
import UserReviewBadge from '../UserReviewBadge/UserReviewBadge';
import { UsersReviewsCardPropsType } from './UsersReviewsCardTypes';
import styles from './UsersReviewsCard.module.scss'

const reviews: ReviewGetTypes[] = [
  {uuid: '1', text: 'Очень хороший сайт', stars: 5, datatime: '21.01.2017'},
  {uuid: '2', text: 'Хороший сайт', stars: 4, datatime: '27.02.2018'},
  {uuid: '3', text: '', stars: 2, datatime: '27.02.2019'},
  {uuid: '4', text: 'Мне нравится', stars: 5, datatime: '27.02.2019'},
  {uuid: '5', text: 'Да', stars: 1, datatime: '27.02.2019'},
]

const UsersReviewsCard = ({sourceUuid, ...props}: UsersReviewsCardPropsType) => {
  const {data: reviews, isLoading} = useGetAllReviewsQuery()

  if (isLoading) {
    return null
  }

  return (
    <Card 
      title='Отзывы, которые пользователи оставили об этом ресурсе'
      description='Читайте, что думают об этом ресурсе другие люди'
      {...props}
    >
      <>
        {reviews?.length ?
        reviews.map(review => <UserReviewBadge key={review.uuid} {...review}/>) : <span className={styles.no_reviews}>Отзывов нет</span>}
      </>
    </Card>
  );
};

export default UsersReviewsCard;