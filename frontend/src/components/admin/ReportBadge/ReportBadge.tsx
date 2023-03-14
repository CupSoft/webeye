import React from 'react';
import styles from './ReportBadge.module.scss'
import cn from 'classnames'
import { ReportBadgePropsType } from './ReportBadgeTypes';
const resource = ''
const text = 'Не работает сайт'
const ReportBadge = ({status, is_moderated}: ReportBadgePropsType) => {
  return (
    <div className={styles.container}>
      <span className={styles.title}>
        <span className={cn(styles.state, styles[status.toLowerCase()])}></span>
        <span className={styles.resource}>HSE</span>
        <span className={styles.date}>{new Date().toLocaleDateString()}</span>
      </span>
      <hr/>
      {text && <span className={styles.text}>{text}</span>}
    </div>
  );
};

export default ReportBadge;