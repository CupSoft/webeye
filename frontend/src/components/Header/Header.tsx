import styles from './Header.module.scss';
import cn from 'classnames'
import { NavLink, useNavigate } from 'react-router-dom';
import { AUTH_ROUTE, MAIN_ROUTE, SOURCES_ROUTE } from '../../utils/constants';
import Button from '../UI/Button/Button';
import { useAppDispatch, useAppSelector } from '../../app/hooks';
import { isAuthSelector } from '../../app/selectors/isAuthSelector';

const Header = () => {
  const navigate = useNavigate()
  const dispatch = useAppDispatch()
  const isAuth = useAppSelector(isAuthSelector)

  function signInClickHandler() {
    if (isAuth) {
      dispatch({type: 'auth', payload: false})
      navigate(MAIN_ROUTE)
      
    } else {
      navigate(AUTH_ROUTE)
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