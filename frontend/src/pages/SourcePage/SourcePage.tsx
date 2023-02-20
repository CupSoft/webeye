import cn from 'classnames';
import { useParams } from 'react-router-dom';
import ReviewCard from '../../components/ReviewCard/ReviewCard';
import SocialNetworksCard from '../../components/SocialNetworksCard/SocialNetworksCard';
import StateChart from '../../components/StateChart/StateChart';
import SubscriptionCard from '../../components/SubscriptionCard/SubscriptionCard';
import Button from '../../components/UI/Button/Button';
import UsersReviewsCard from '../../components/UsersReviewsCard/UsersReviewsCard';
import { useGetSourceQuery } from '../../services/apiService/apiService';
import NotFoundPage from '../NotFoundPage/NotFoundPage';
import styles from './SourcePage.module.scss';

let source = {uuid: '1', name: 'Вышка', status: 'OK', rating: 4.92}

const SourcePage = () => {
  const params = useParams()
  const uuid = params.uuid ?? ''
  
  let {data: source, isLoading} = useGetSourceQuery(uuid)
  
  if (!source) {
    return <NotFoundPage/>
  }

  if (isLoading) {
    return null;
  }
  function summaryClickHandler() {
    console.log('getSummary')
  }

  return (
    <div className={styles.container}>
      <div className={styles.title}>
        <h1 
          className={
            cn("page_title", styles.status, styles[source.status.toLowerCase()])
          }
        >
          {uuid ? source.name : 'Ресурс'}
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