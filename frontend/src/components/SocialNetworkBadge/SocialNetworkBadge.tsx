import cn from 'classnames';
import styles from './SocialNetworkBadge.module.scss';
import { SocialNetworkBadgePropsType } from './SocialNetworkBadgeTypes';

const SocialNetworkBadge = ({link, social_network, snippet, status, created_at}: SocialNetworkBadgePropsType) => {
  console.log()
  return (
    <a href={link} target="_blank" rel="noreferrer" className={styles.container}>
      <span className={styles.title}>
        <span className={cn(styles.state, styles[status.toLowerCase()])}></span>
        <span 
          className={
            cn(styles.social, styles[social_network.toLowerCase()])
          }
        />
        <span className={styles.date}>
          {new Date(created_at).toLocaleDateString()}
        </span>
      </span>
      <hr/>
      {snippet && <span className={styles.text}>{snippet}</span>}
    </a>
  );
};

export default SocialNetworkBadge;