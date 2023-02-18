import Card from '../Card/Card';
import SocialNetworkBadge from '../SocialNetworkBadge/SocialNetworkBadge';
import { SocialNetworksCardPropsType } from './SocialNetworksCardTypes';

const cards = [
  {id: 1, link: 'https://vk.com', social: 'vk', state: 'critical', text: 'Вообще не работает'},
  {id: 2, link: 'https://ok.ru', social: 'ok', state: 'partial', text: 'Работает частично'},
  {id: 3, link: 'https://ok.ru', social: 'ok', state: 'ok', text: 'Работает стабильно'},
  {id: 4, link: 'https://ok.ru', social: 'ok', state: 'ok', text: 'Работает стабильно'},
  {id: 5, link: 'https://ok.ru', social: 'ok', state: 'ok', text: 'Работает стабильно'},
]

const SocialNetworksCard = ({sourceId, ...props}: SocialNetworksCardPropsType) => {
  return (
    <Card 
      title='Что пишут люди об этом ресурсе в социальных сетях?'
      description='Просматривайте актуальные сообщения от пользователей'
      {...props}
    >
      <>
        {cards.map(card => <SocialNetworkBadge key={card.id} {...card}/>)}
      </>
    </Card>
  );
};

export default SocialNetworksCard;