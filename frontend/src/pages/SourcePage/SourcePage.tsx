import cn from 'classnames';
import { useParams } from 'react-router-dom';
import ReviewCard from '../../components/ReviewCard/ReviewCard';
import SocialNetworksCard from '../../components/SocialNetworksCard/SocialNetworksCard';
import StateChart from '../../components/StateChart/StateChart';
import SubscriptionCard from '../../components/SubscriptionCard/SubscriptionCard';
import Button from '../../components/UI/Button/Button';
import UsersReviewsCard from '../../components/UsersReviewsCard/UsersReviewsCard';
import styles from './SourcePage.module.scss';

const sources = [
  {uuid: '1', name: 'Вышка', state: 'ok', rating: 4.92},
  {uuid: '2', name: 'МГТУ Баумана', state: 'critical', rating: 4.78},
  {uuid: '3', name: 'МФТИ', state: 'partial', rating: 4.95},
  {uuid: '4', name: 'Вышка', state: 'ok', rating: 4.92},
  {uuid: '5', name: 'МГТУ Баумана', state: 'critical', rating: 4.78},
  {uuid: '6', name: 'МФТИ', state: 'partial', rating: 4.95},
  {uuid: '7', name: 'Вышка', state: 'ok', rating: 4.92},
  {uuid: '8', name: 'МГТУ Баумана', state: 'critical', rating: 4.78},
  {uuid: '9', name: 'МФТИ', state: 'partial', rating: 4.95},
  {uuid: '10', name: 'МФТИ', state: 'partial', rating: 4.95},
]

const SourcePage = () => {
  const params = useParams()
  const uuid = params.uuid ? +params.uuid - 1 : -1
  const source = sources[uuid]

  function summaryClickHandler() {
    console.log('getSummary')
  }

  return (
    <div className={styles.container}>
      <div className={styles.title}>
        <h1 
          className={
            cn("page_title", styles.state, styles[source.state.toLowerCase()])
          }
        >
          {uuid !== -1 ? source.name : 'Ресурс'}
        </h1>
        <span className={styles.rating}>{source.rating}</span>
        <Button btnType='turquoise' onClick={summaryClickHandler}>
          <span className={styles.download_btn}>Получить отчёт</span>
        </Button>
      </div>
      <StateChart sourceUuid={source.uuid}/>
      <div className={styles.cards}>
        <ReviewCard sourceUuid={source.uuid}/>
        <UsersReviewsCard sourceUuid={source.uuid}/>
        <SocialNetworksCard sourceUuid={source.uuid}/>
        <SubscriptionCard sourceUuid={source.uuid}/>
      </div>
    </div>
  );
};

export default SourcePage;