import { useEffect } from 'react';
import { useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { userSelector } from '../../app/selectors/userSelector';
import { AUTH_ROUTE } from '../../utils/constants';
import styles from './AdminPage.module.scss';

const AdminPage = () => {
  const {isAuth} = useSelector(userSelector)
  const navigate = useNavigate()

  useEffect(() => {
    if (!isAuth) {
      navigate(AUTH_ROUTE + '?next_page=/admin')
    }
  }, [])

  return (
    <div className={styles.container}>
      
    </div>
  );
};

export default AdminPage;