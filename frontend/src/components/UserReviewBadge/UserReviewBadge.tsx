import React from 'react';
import { UserReviewBadgePropsType } from './UserReviewBadgeTypes';
import styles from './UserReviewBadge.module.scss';

const UserReviewBadge = ({text, date, stars}: UserReviewBadgePropsType) => {
  return (
    <div className={styles.container}>
      {text}
    </div>
  );
};

export default UserReviewBadge;