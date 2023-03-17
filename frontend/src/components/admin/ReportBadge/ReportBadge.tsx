import cn from 'classnames';
import styles from './ReportBadge.module.scss';
import { ReportBadgePropsType } from './ReportBadgeTypes';

const ReportBadge = ({status, is_moderated, text, created_at, resource_name}: ReportBadgePropsType) => {
  return (
    <>
    {!is_moderated && status === 'critical' &&
      <div className={styles.container}>
        <span className={styles.title}>
          <span className={cn(styles.state, styles[status.toLowerCase()])}></span>
          <span className={styles.resource}>{resource_name ?? 'Нет ресурса'}</span>
          <span className={styles.date}>{created_at ? new Date(created_at).toLocaleDateString() : 'Нет даты'}</span>
        </span>
        <hr/>
        <span className={styles.text}>{text ?? 'Нет текста'}</span>
      </div>
    }
    </>
  );
};

export default ReportBadge;