import cn from 'classnames';
import { NavLink, useLocation, useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import { useAppDispatch, useAppSelector } from '../../app/hooks';
import { userSelector } from '../../app/selectors/userSelector';
import { useGetBotTokenMutation } from '../../services/apiService/apiService';
import { AUTH_ROUTE, MAIN_ROUTE, SOURCES_ROUTE } from '../../utils/constants';
import Button from '../UI/Button/Button';
import styles from './Header.module.scss';

const Header = () => {
  const navigate = useNavigate()
  const dispatch = useAppDispatch()
  const {isAuth} = useAppSelector(userSelector)
  const location = useLocation()
  const [getBotToken] = useGetBotTokenMutation()

  function signInClickHandler() {
    if (isAuth) {
      dispatch({type: 'changeUser', payload: {isAuth: false, email: '', isAdmin: false, uuid: ''}})
      localStorage.removeItem('token')
    } else {
      if (location.pathname !== '/auth') {
        navigate(AUTH_ROUTE + `?next_page=${location.pathname}`)
      }
    }
  }

  function botClickHandler() {
    if (!isAuth) {
      window.open(`${process.env.REACT_APP_BOT_LINK}`, '_blank')
      return
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
    <>
      <div className={cn(styles.header)}>
        <span className={cn(styles.navigation)}>
          <NavLink to={MAIN_ROUTE}>Главная</NavLink>
          <NavLink to={SOURCES_ROUTE}>Все ВУЗы</NavLink>
        </span>
        <span className={cn(styles.title)}>
          <NavLink to={MAIN_ROUTE}>WebEye</NavLink>
        </span>
        <span className={cn(styles.buttons)}>
          <Button 
            btnType={'blue'}
            noWrap={true}
            onClick={botClickHandler}
          >Телеграм бот</Button>
          <Button
            size='md'
            onClick={signInClickHandler}
          >{isAuth ? 'Выйти' : 'Войти'}</Button>
        </span>
      </div>
      <hr/>
    </>
  );
};

export default Header;