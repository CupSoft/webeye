import styles from './Card.module.scss';
import communityIcon from './../../assets/cardIcons/communityIcon.svg';
import handshakeIcon from './../../assets/cardIcons/handshakeIcon.svg';
import sourcesIcon from './../../assets/cardIcons/sourcesIcon.svg';
import { IconsType } from './CardTypes';
import cn from 'classnames'

const icons: IconsType = {
  community: communityIcon,
  handshake: handshakeIcon,
  sources: sourcesIcon,
}

const Card = ({icon='', size='sm', title='Карточка', children='', ...props}) => {
  return (
    <div className={cn(styles.container, styles[size])} {...props}>
      {icon && <img className={styles.icon} src={icons[icon]} alt='Сообщество'/>}
      <span className={styles.title}>{title}</span>
      <span className={styles.body}>{children}</span>
    </div>
  );
};

export default Card;