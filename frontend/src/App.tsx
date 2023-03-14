import { useEffect, useState } from 'react';
import { ToastContainer } from 'react-toastify';
import styles from './App.module.scss';
import { useAppDispatch } from './app/hooks';
import AppRouter from './components/AppRouter/AppRouter';
import Header from './components/Header/Header';
import ColorCircle from './components/UI/ColorCircle/ColorCircle';
import { useCheckUserMutation } from './services/apiService/apiService';

let prevPageX = 0
let prevPageY = 0

function App() {
  const dispatch = useAppDispatch()
  const [checkUser, {isLoading}] = useCheckUserMutation()
  const [moveIndicator, setMoveIndicator] = useState({x: 0, y: 0})

  function mouseMoveHandler(evt: React.MouseEvent) {
    const x = evt.pageX - prevPageX
    const y = evt.pageY - prevPageY

    setMoveIndicator({x, y})

    prevPageX = evt.pageX
    prevPageY = evt.pageY
  }

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
    <div className={styles.app} onMouseMove={mouseMoveHandler}>
      <Header/>
      <AppRouter/>
      <ToastContainer
          position="top-right"
          autoClose={2500}
          hideProgressBar={false}
          newestOnTop={false}
          closeOnClick
          rtl={false}
          pauseOnFocusLoss
          draggable
          pauseOnHover
          theme="dark"
        />
        <ColorCircle color='blue' position='left' moveIndicator={moveIndicator}/>
        <ColorCircle color='yellow' position='right' moveIndicator={moveIndicator}/>
    </div>
  );
}

export default App;
