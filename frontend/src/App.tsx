import { useEffect } from 'react';
import styles from './App.module.scss';
import { useAppDispatch } from './app/hooks';
import AppRouter from './components/AppRouter/AppRouter';
import Header from './components/Header/Header';
import { useCheckUserMutation } from './services/apiService/apiService';

function App() {
  const dispatch = useAppDispatch()
  const [checkUser, {data, isLoading}] = useCheckUserMutation()

  useEffect(() => {
    checkUser().then(value => {
      if ('error' in value) {
        return
      }

      const {uuid, email, is_admin} = value.data
      dispatch({
        type: 'changeUser', 
        payload: {
          uuid,
          email,
          isAdmin: is_admin,
          isAuth: true
        }
      })
    })
  }, [])

  if (isLoading) {
    return null
  }

  return (
    <div className={styles.app}>
      <Header/>
      <AppRouter/>
    </div>
  );
}

export default App;
