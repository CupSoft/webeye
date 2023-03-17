import React from 'react';
import { useGetAllSocialReportsQuery } from '../../../services/apiService/apiService';
import SocialNetworkBadge from '../../SocialNetworkBadge/SocialNetworkBadge';
import styles from './SocialReportsList.module.scss';
import { SocialReportsPropsType } from './SocialReportsListTypes';

const SocialReportsList = ({sourceUuid}: SocialReportsPropsType) => {
  const {data: cards, isLoading} = useGetAllSocialReportsQuery(sourceUuid)

  if (isLoading) {
    return null
  }

  return (
    <div className={styles.container}>
      {/* <span className={styles.title}>В социальных сетях</span> */}
      {cards?.length ?
        cards.map(card => <SocialNetworkBadge key={card.uuid} {...card}/>)
      : <span className={styles.no_social_reports}>
        Сообщений нет
      </span>}
    </div>
  );
};

export default SocialReportsList;