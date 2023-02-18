import React from 'react';
import { UserReviewBadgePropsType } from './UserReviewBadgeTypes';
import styles from './UserReviewBadge.module.scss';

const UserReviewBadge = ({text, date, stars}: UserReviewBadgePropsType) => {
  return (
    <div className={styles.container}>
      <span className={styles.title}>
        <span className={styles.date}>{date}</span>
        <span className={styles.stars}>{stars}</span>
      </span>
      <hr/>
      <span className={styles.text}>{text}</span>
    </div>
  );
};

export default UserReviewBadge;