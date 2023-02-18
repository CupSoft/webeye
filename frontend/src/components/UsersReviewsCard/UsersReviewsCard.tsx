import Card from '../Card/Card';
import UserReviewBadge from '../UserReviewBadge/UserReviewBadge';
import { UsersReviewsCardPropsType } from './UsersReviewsCardTypes';

const reviews = [
  {id: 1, text: 'Очень хороший сайт', stars: 5, date: '21.01.2017'},
]

const UsersReviewsCard = ({sourceId, ...props}: UsersReviewsCardPropsType) => {
  return (
    <Card 
      title='Отзывы, которые пользователи оставили об этом ресурсе'
      description='Читайте, что думают об этом ресурсе другие люди'
      {...props}
    >
      <>
        {reviews.map(review => <UserReviewBadge key={review.id} {...review}/>)}
      </>
    </Card>
  );
};

export default UsersReviewsCard;