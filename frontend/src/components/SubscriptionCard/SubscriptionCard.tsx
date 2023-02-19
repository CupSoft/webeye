import cn from 'classnames';
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAppSelector } from '../../app/hooks';
import { userSelector } from '../../app/selectors/userSelector';
import { AUTH_ROUTE, SOURCES_ROUTE } from '../../utils/constants';
import Card from '../Card/Card';
import styles from './SubscriptionCard.module.scss';
import { SubscriptionCardPropsType } from './SubscriptionCardTypes';

const SubscriptionCard = ({sourceUuid, ...props}: SubscriptionCardPropsType) => {
  const [emailChecked, setEmailChecked] = useState(false)
  const [botChecked, setBotChecked] = useState(false)
  const isAuth = useAppSelector(userSelector)
  const navigate = useNavigate()

  function authClickHandler() {
    navigate(AUTH_ROUTE + `?next_page=${SOURCES_ROUTE + '/' + sourceUuid}`)
  }

  function onCheckChange(event: React.ChangeEvent<HTMLInputElement>) {
    if (!isAuth) {
      return
    }
    if (event.target.name === 'bot_sub') {
      setBotChecked(!botChecked)
    } else {
      setEmailChecked(!emailChecked)
    }
  }

  return (
    <Card 
      title={
      <span>
        {!isAuth && 
        <u
          style={{cursor: 'pointer'}} 
          onClick={authClickHandler}
        >Авторизуйтесь</u>}
        {isAuth ? 'П' : ' и п'}одпишитесь на уведомления о недоступности ресурса
      </span>
      }
      description='Подписывайтесь на сообщения о недоступности ресурсов по почте и посредством телеграм бота'
      bodyFlexStart={true}
      {...props}
    >
      <>
        <label 
          htmlFor="bot_sub" 
          className={cn(styles.checkbox_label, !isAuth && styles.not_auth)}
        >
          <input 
            className={styles.checkbox}
            type="checkbox"
            name="bot_sub"
            checked={botChecked}
            onChange={onCheckChange}
            id="bot_sub"
          />
          <span className={cn(styles.checkbox_text, 'noselect')}>
            Получать уведомления посредством телеграм бота
            <i 
              className={styles.tg_description}
            >*не забудьте авторизоваться в<u><a href='#'>телеграм боте</a></u></i>
          </span>
        </label>
        <label 
          htmlFor="email_sub" 
          className={cn(styles.checkbox_label, !isAuth && styles.not_auth)}
        >
          <input
            className={styles.checkbox}
            type="checkbox"
            name="email_sub"
            checked={emailChecked}
            onChange={onCheckChange}
            id="email_sub"
          />
          <span className={cn(styles.checkbox_text, 'noselect')}>
            Получать уведомления по почте
          </span>
        </label>
      </>
    </Card>
  );
};

export default SubscriptionCard;