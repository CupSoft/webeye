import { useGetAllSocialReportsQuery } from '../../services/apiService/apiService';
import Card from '../Card/Card';
import SocialNetworkBadge from '../SocialNetworkBadge/SocialNetworkBadge';
import styles from './SocialNetworksCard.module.scss';
import { SocialNetworksCardPropsType } from './SocialNetworksCardTypes';

const SocialNetworksCard = ({sourceUuid, ...props}: SocialNetworksCardPropsType) => {
  const {data: cards, isLoading} = useGetAllSocialReportsQuery(sourceUuid)

  if (isLoading) {
    return null
  }

  return (
    <Card 
      title='Что пишут люди об этом ресурсе в социальных сетях?'
      description='Просматривайте актуальные сообщения от пользователей'
      {...props}
    >
      <>
        {cards?.length ?
          cards.map(card => <SocialNetworkBadge key={card.uuid} {...card}/>)
        : <span className={styles.no_social_reports}>
          Сообщений нет
          </span>}
      </>
    </Card>
  );
};

export default SocialNetworksCard;