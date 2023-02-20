import cn from 'classnames';
import React, { useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAppSelector } from '../../app/hooks';
import { userSelector } from '../../app/selectors/userSelector';
import { useGetSubscriptionsQuery, usePatchSubscriptionsMutation, usePostSubscriptionsMutation } from '../../services/apiService/apiService';
import { AUTH_ROUTE, SOURCES_ROUTE } from '../../utils/constants';
import Card from '../Card/Card';
import styles from './SubscriptionCard.module.scss';
import { SubscriptionCardPropsType } from './SubscriptionCardTypes';

const SubscriptionCard = ({sourceUuid, ...props}: SubscriptionCardPropsType) => {
  const {isAuth} = useAppSelector(userSelector)
  const navigate = useNavigate()
  const [postSubscriptions] = usePostSubscriptionsMutation()
  const [patchSubscriptions] = usePatchSubscriptionsMutation()
  const {data: subs, isLoading} = useGetSubscriptionsQuery(sourceUuid)

  if (isLoading) {
    return null
  }
  console.log(subs)


  function authClickHandler() {
    navigate(AUTH_ROUTE + `?next_page=${SOURCES_ROUTE + '/' + sourceUuid}`)
  }

  function onCheckChange(event: any) {
    let to_email
    let to_telegram

    if (event.target.name === 'bot_sub') {
      to_email = (event.target.parentElement?.parentElement?.querySelector('#email_sub') as HTMLInputElement)?.checked
      to_telegram = event.target.checked
    } else {
      to_email = event.target.checked
      to_telegram = (event.target.parentElement?.parentElement?.querySelector('#bot_sub') as HTMLInputElement)?.checked
    }

    if (subs === undefined || subs.length === 0) {
      postSubscriptions({
        resource_uuid: sourceUuid,
        to_email,
        to_telegram
      })

      return;
    }

    patchSubscriptions({
      to_email,
      to_telegram,
      uuid: subs[0].uuid
    })
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
            onClick={onCheckChange}
            id="bot_sub"
            defaultChecked={subs && !!subs[0].to_telegram}
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
            onChange={onCheckChange}
            id="email_sub"
            defaultChecked={subs && !!subs[0].to_email}
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