import cn from 'classnames';
import Button from '../../UI/Button/Button';
import styles from './ReportBadge.module.scss';
import { ReportBadgePropsType } from './ReportBadgeTypes';

const ReportBadge = ({uuid, status, is_moderated, text, created_at, resource_name, deleteClickHandler}: ReportBadgePropsType) => {
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
        <div className={styles.moderate_btns}>
          <Button 
            myClass={styles.approve_btn}
            btnType='green'
            noWrap={true}
            onClick={deleteClickHandler}
          ><span></span></Button>
          <Button 
            myClass={styles.delete_btn}
            btnType='red'
            noWrap={true}
            onClick={deleteClickHandler}
          ><span></span></Button>
        </div>
      </div>
    }
    </>
  );
};

export default ReportBadge;