import styles from './Card.module.scss';
import communityIcon from './../../assets/cardIcons/communityIcon.svg';
import handshakeIcon from './../../assets/cardIcons/handshakeIcon.svg';
import sourcesIcon from './../../assets/cardIcons/sourcesIcon.svg';
import { CardPropsType, IconsType } from './CardTypes';
import cn from 'classnames'

const icons: IconsType = {
  community: communityIcon,
  handshake: handshakeIcon,
  sources: sourcesIcon,
}

const Card = ({icon='', size='sm', title='Карточка', description='', bodyFlexStart=false,children='', ...props}: CardPropsType) => {
  return (
    <div className={cn(styles.container, styles[size])} {...props}>
      {icon && <img className={styles.icon} src={icons[icon]} alt='Сообщество'/>}
      {title && <span className={styles.title}>{title}</span>}
      {description && <span className={styles.description}>{description}</span>}
      {children && 
      <span 
        className={cn(styles.body, bodyFlexStart && styles.start)}
      >{children}</span>}
    </div>
  );
};

export default Card;