import styles from './Header.module.scss';
import cn from 'classnames'
import { NavLink, useNavigate } from 'react-router-dom';
import { AUTH_ROUTE, MAIN_ROUTE, SOURCES_ROUTE } from '../../utils/constants';
import Button from '../UI/Button/Button';

const Header = () => {
  const navigate = useNavigate()

  const isAuth = false

  function signInClickHandler() {
    navigate(AUTH_ROUTE)
  }

  return (
    <>
      <div className={cn(styles.header)}>
        <span className={cn(styles.navigation, 'row')}>
          <NavLink to={MAIN_ROUTE}>Главная</NavLink>
          <NavLink to={SOURCES_ROUTE}>Все ВУЗы</NavLink>
        </span>
        <span className={cn(styles.title)}>
          <NavLink to={MAIN_ROUTE}>WebEye</NavLink>
        </span>
        <span className={cn(styles.buttons)}>
          <Button btnType={'blue'}>Телеграм бот</Button>
          {!isAuth && 
            <Button
              size={'lg'}
              onClick={signInClickHandler}
            >Вход</Button>
          }
        </span>
      </div>
      <hr/>
    </>
  );
};

export default Header;