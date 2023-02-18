import React from 'react';
import styles from './SocialNetworkCard.module.scss'
import { IconsType, SocialNetworkCardPropsType } from './SocialNetworkCardTypes';
import vkIcon from './../../assets/socialIcons/vkIcon.svg';
import cn from 'classnames'
import { Link } from 'react-router-dom';

const SocialNetworkCard = ({link, social, text, state}: SocialNetworkCardPropsType) => {
  return (
    <a href={link} target="_blank" rel="noreferrer" className={styles.container}>
      <span className={cn(styles.social, styles[social])} />
      <hr/>
      <span className={styles.text}>{text}</span>
    </a>
  );
};

export default SocialNetworkCard;