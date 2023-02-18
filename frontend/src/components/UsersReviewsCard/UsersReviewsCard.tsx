import Card from '../Card/Card';
import UserReviewBadge from '../UserReviewBadge/UserReviewBadge';
import { UsersReviewsCardPropsType } from './UsersReviewsCardTypes';

const reviews = [
  {id: 1, text: 'Очень хороший сайт', stars: 5, date: '21.01.2017'},
  {id: 2, text: 'Хороший сайт', stars: 4, date: '27.02.2018'},
  {id: 3, text: '', stars: 2, date: '27.02.2019'},
  {id: 4, text: 'Мне нравится', stars: 5, date: '27.02.2019'},
  {id: 5, text: 'Да', stars: 1, date: '27.02.2019'},
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