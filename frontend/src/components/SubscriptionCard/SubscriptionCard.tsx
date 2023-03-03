import cn from 'classnames';
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import { useAppSelector } from '../../app/hooks';
import { userSelector } from '../../app/selectors/userSelector';
import { useGetBotTokenMutation, useGetSubscriptionsMutation, usePatchSubscriptionsMutation, usePostSubscriptionsMutation } from '../../services/apiService/apiService';
import { AUTH_ROUTE, SOURCES_ROUTE } from '../../utils/constants';
import Card from '../Card/Card';
import styles from './SubscriptionCard.module.scss';
import { SubscriptionCardPropsType } from './SubscriptionCardTypes';

const SubscriptionCard = ({sourceUuid, ...props}: SubscriptionCardPropsType) => {
  const {isAuth} = useAppSelector(userSelector)
  const navigate = useNavigate()
  const [subs, setSubs] = useState({to_email: false, to_telegram: false, uuid: ''})
  const [postSubscriptions] = usePostSubscriptionsMutation()
  const [patchSubscriptions] = usePatchSubscriptionsMutation()
  let [getSubscriptions] = useGetSubscriptionsMutation()
  const [getBotToken] = useGetBotTokenMutation()

  function authClickHandler() {
    navigate(AUTH_ROUTE + `?next_page=${SOURCES_ROUTE + '/' + sourceUuid}`)
  }

  useEffect(() => {
    getSubscriptions(sourceUuid).then(value => {
      if ('error' in value) {
        return
      }

      const curSubs = value.data[0]
      
      if (!curSubs) {
        postSubscriptions({
          ...subs, resource_uuid: sourceUuid
        }).then(value => {
          if ('error' in value) {
            toast('Не уадлось получить ваши подписки')
            return
          }

          setSubs(value.data)
        })
      } else {
        setSubs({
          to_email: curSubs.to_email, 
          to_telegram: curSubs.to_telegram,
          uuid: curSubs.uuid
        })
      }
    })
  }, [])

  function onCheckChange(event: React.ChangeEvent<HTMLInputElement>) {
    if (!isAuth) {
      event.preventDefault();
      return
    }

    const newSubs = {...subs, [event.target.name]: event.target.checked}
    setSubs(newSubs)
    patchSubscriptions({
      ...newSubs
    }).then(value => {
      if ('error' in value) {
        toast('Не удалось обновить ваши подписки')
        return
      }
      toast('Ваши подписки успешно обновлены')
    })
  }

  function botClickHandler(event: React.MouseEvent) {
    event.preventDefault();
    if (!isAuth) {
      return;
    }
    getBotToken().then(value => {
      if ('error' in value) {
        toast('Ошибка авторизации бота!')
        return
      }
      
      window.open(`${process.env.REACT_APP_BOT_LINK}?start=${value.data.token}`, '_blank')
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
          htmlFor="to_telegram" 
          className={cn(styles.checkbox_label, !isAuth && styles.not_auth)}
        >
          <input 
            className={styles.checkbox}
            type="checkbox"
            name="to_telegram"
            onChange={onCheckChange}
            id="to_telegram"
            checked={subs.to_telegram}
          />
          <span className={cn(styles.checkbox_text, 'noselect')}>
            Получать уведомления посредством телеграм бота
            <i 
              className={styles.tg_description}
            >*не забудьте авторизоваться в<u 
              onClick={botClickHandler}
              className={cn(!isAuth && styles.not_bot_auth)}
            >телеграм боте</u></i>
          </span>
        </label>
        <label 
          htmlFor="to_email" 
          className={cn(styles.checkbox_label, !isAuth && styles.not_auth)}
        >
          <input
            className={styles.checkbox}
            type="checkbox"
            name="to_email"
            onChange={onCheckChange}
            id="to_email"
            checked={subs.to_email}
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