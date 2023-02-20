import cn from 'classnames';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import { useAppSelector } from '../../app/hooks';
import { userSelector } from '../../app/selectors/userSelector';
import { useGetBotTokenMutation, useGetSubscriptionsQuery, usePatchSubscriptionsMutation, usePostSubscriptionsMutation } from '../../services/apiService/apiService';
import { AUTH_ROUTE, SOURCES_ROUTE, TG_BOT_LINK } from '../../utils/constants';
import Card from '../Card/Card';
import styles from './SubscriptionCard.module.scss';
import { SubscriptionCardPropsType } from './SubscriptionCardTypes';

const SubscriptionCard = ({sourceUuid, ...props}: SubscriptionCardPropsType) => {
  const {isAuth} = useAppSelector(userSelector)
  const navigate = useNavigate()
  const [postSubscriptions] = usePostSubscriptionsMutation()
  const [patchSubscriptions] = usePatchSubscriptionsMutation()
  let {data: subs, isLoading} = useGetSubscriptionsQuery(sourceUuid)
  const [getBotToken] = useGetBotTokenMutation()

  if (isLoading) {
    return null
  }

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
    console.log(subs)
    if (subs?.length === 0 || subs === undefined) {
      postSubscriptions({
        resource_uuid: sourceUuid,
        to_email,
        to_telegram
      }).then(value => {
        if ('error' in value) {
          toast('Не удалось подписаться - подпишитесь повторно!')
          return
        }
        const {to_email, to_telegram, uuid} = value.data
        subs = [{to_email, to_telegram, uuid}]
        toast('Вы успешно подписались!')
      })

      return;
    }

    patchSubscriptions({
      to_email,
      to_telegram,
      uuid: subs[0].uuid
    }).then(value => {
      if ('error' in value) {
        toast('Не удалось подписаться - подпишитесь повторно!')
        return
      }
      toast('Вы успешно подписались!')
    })
  }

  function botClickHandler(event: React.MouseEvent) {
    event.preventDefault();
    getBotToken().then(value => {
      if ('error' in value) {
        toast('Ошибка авторизации бота!')
        return
      }
      
      window.open(`${TG_BOT_LINK}?start=${value.data.token}`, '_blank')
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
            defaultChecked={subs && !!subs[0]?.to_telegram}
          />
          <span className={cn(styles.checkbox_text, 'noselect')}>
            Получать уведомления посредством телеграм бота
            <i 
              className={styles.tg_description}
            >*не забудьте авторизоваться в<u onClick={botClickHandler}>телеграм боте</u></i>
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
            defaultChecked={subs && !!subs[0]?.to_email}
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