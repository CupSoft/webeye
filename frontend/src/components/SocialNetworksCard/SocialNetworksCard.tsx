import { useGetAllSocialReportsQuery } from '../../services/apiService/apiService';
import { SocialReportsGetTypes } from '../../services/apiService/apiServiceTypes';
import Card from '../Card/Card';
import SocialNetworkBadge from '../SocialNetworkBadge/SocialNetworkBadge';
import { SocialNetworksCardPropsType } from './SocialNetworksCardTypes';
import styles from './SocialNetworksCard.module.scss'

const cards: SocialReportsGetTypes[] = [
  {uuid: '1', link: 'https://vk.com', social_network: 'OK', status: 'critical', snippet: 'Вообще не работает', created_at: '2023-02-19T09:50:41.783Z'},
  {uuid: '2', link: 'https://ok.ru', social_network: 'OK', status: 'partial', snippet: 'Работает частично', created_at: '2023-02-19T09:50:41.783Z'},
  {uuid: '3', link: 'https://ok.ru', social_network: 'OK', status: 'OK', snippet: 'Работает стабильно', created_at: '2023-02-19T09:50:41.783Z'},
  {uuid: '4', link: 'https://ok.ru', social_network: 'VK', status: 'OK', snippet: 'Работает стабильно', created_at: '2023-02-19T09:50:41.783Z'},
  {uuid: '5', link: 'https://ok.ru', social_network: 'OK', status: 'OK', snippet: 'Работает стабильно', created_at: '2023-02-19T09:50:41.783Z'},
]

const SocialNetworksCard = ({sourceUuid, ...props}: SocialNetworksCardPropsType) => {
  const {data: cards, isLoading} = useGetAllSocialReportsQuery()

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