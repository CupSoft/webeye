import styles from './Header.module.scss';
import cn from 'classnames'
import { NavLink, useLocation, useNavigate } from 'react-router-dom';
import { AUTH_ROUTE, MAIN_ROUTE, SOURCES_ROUTE } from '../../utils/constants';
import Button from '../UI/Button/Button';
import { useAppDispatch, useAppSelector } from '../../app/hooks';
import { userSelector } from '../../app/selectors/userSelector';

const Header = () => {
  const navigate = useNavigate()
  const dispatch = useAppDispatch()
  const {isAuth} = useAppSelector(userSelector)
  const location = useLocation()

  function signInClickHandler() {
    if (isAuth) {
      dispatch({type: 'changeUser', payload: {isAuth: false, email: '', isAdmin: false, uuid: ''}})
      localStorage.removeItem('token')
    } else {
      navigate(AUTH_ROUTE + `?next_page=${location.pathname}`)
    }
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
          <Button btnType={'blue'}>Телеграм бот</Button>
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