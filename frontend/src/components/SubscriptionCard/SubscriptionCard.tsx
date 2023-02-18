import React from 'react';
import Card from '../Card/Card';
import styles from './SubscriptionCard.module.scss'
import { SubscriptionCardPropsType } from './SubscriptionCardTypes';

const SubscriptionCard = ({sourceId, ...props}: SubscriptionCardPropsType) => {
  return (
    <Card 
      title='Подпишитесь на уведомления о недоступности ресурса'
      description='Подписывайтесь на сообщения о недоступности ресурсов по почте и посредством телеграм бота'
      {...props}
    >
    </Card>
  );
};

export default SubscriptionCard;