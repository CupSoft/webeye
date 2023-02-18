import cn from 'classnames';
import styles from './SocialNetworkBadge.module.scss';
import { SocialNetworkBadgePropsType } from './SocialNetworkBadgeTypes';

const SocialNetworkBadge = ({link, social, text, state}: SocialNetworkBadgePropsType) => {
  return (
    <a href={link} target="_blank" rel="noreferrer" className={styles.container}>
      <span className={styles.title}>
        <span className={cn(styles.state, styles[state.toLowerCase()])}></span>
        <span 
          className={
            cn(styles.social, styles[social])
          }
        />
      </span>
      <hr/>
      <span className={styles.text}>{text}</span>
    </a>
  );
};

export default SocialNetworkBadge;