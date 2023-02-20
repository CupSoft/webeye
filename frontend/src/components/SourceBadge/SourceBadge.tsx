import { Link } from 'react-router-dom';
import { SOURCES_ROUTE } from '../../utils/constants';
import styles from './SourceBadge.module.scss'
import cn from 'classnames'
import { SourceCardPropsType } from './SourceBadgeTypes';

const SourceCard = ({uuid, status='OK', name='ВУЗ', rating=4.78, i=0, ...props}: SourceCardPropsType) => {
  return (
    <div className={styles.container} {...props}>
      <span className={styles.position}>{i + 1}.</span>
      <span className={styles.name}>
        <Link to={SOURCES_ROUTE + '/' + uuid}>{name}</Link>
      </span>
      <span className={cn(styles.vr, styles.first_vr)}/>
      <span 
        className={cn(styles.state, styles[status.toLowerCase()])}
      >{status}</span>
      <span className={styles.vr}></span>
      <span className={styles.rating}>{rating}</span>
    </div>
  );
};

export default SourceCard;