import { BaseSyntheticEvent, RefObject, useRef, useState } from 'react';
import { FieldValues, useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';
import { useAppDispatch } from '../../app/hooks';
import Button from '../../components/UI/Button/Button';
import Input from '../../components/UI/Input/Input';
import { useCheckUserMutation, useLoginUserMutation, useRegisterUserMutation } from '../../services/apiService/apiService';
import { UserRegistrRequestTypes } from '../../services/apiService/apiServiceTypes';
import { emailPattern } from '../../utils/constants';
import { handleLoginUser } from '../../utils/handleLoginUser';
import styles from './AuthPage.module.scss';

const AuthPage = () => {
  const [registerUser] = useRegisterUserMutation()
  const [loginUser] = useLoginUserMutation()
  const [checkUser] = useCheckUserMutation()
  const formRef = useRef<HTMLFormElement>(null)
  const {
    register,
    handleSubmit,
    formState: {errors, isDirty, isValid}
  } = useForm({mode: 'onBlur'})
  const [authError, setAuthError] = useState('')
  const dispatch = useAppDispatch()
  const navigate = useNavigate()
  const params = new URLSearchParams(window.location.search)

  function onEnterDownHanlder(evt: React.KeyboardEvent) {
    if (evt.key !== 'Enter') {
      return
    }
    handleSubmit((data) => onSubmit(data, evt, 'empty'))()
  }

  function onSubmit(
    data: FieldValues, 
    evt: React.KeyboardEvent | BaseSyntheticEvent<object, any, any> | undefined, type: 'login' | 'registr' | 'empty'
  ) {
    if (type === 'empty') {
      return
    }

    const formData = new FormData()

    formData.set('username', data.email)
    formData.set('password', data.password)

    if (type === 'registr') {
      registerUser(data as UserRegistrRequestTypes).then(value => {
        if ('error' in value) {
          setAuthError('Пользователь с таким email уже существует')
          return
        }

        loginUser(formData).then(handleLoginUser(dispatch, navigate, params, setAuthError)).then(() => checkUser().then(value => {
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
        }))
      })
    } else {
      loginUser(formData).then(handleLoginUser(dispatch, navigate, params, setAuthError)).then(() => checkUser().then(value => {
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
      }))
    }
  }

  return (
    <div className={styles.container}>
      <form 
        className={styles.form}
        onKeyDown={onEnterDownHanlder}
        ref={formRef}
      >
        <span className="auth_error">{authError}</span>
        <div className={styles.inputs}>
          <Input
            options={{
              minLength: 1,
              required: true,
              pattern: emailPattern,
              onChange: () => setAuthError('')
            }}
            register={register}
            placeholder="E-mail..."
            name="email"
          />
          <Input
            options={{
              minLength: 1,
              required: true,
              onChange: () => setAuthError('')
            }}
            type='password'
            register={register}
            placeholder="Password..."
            name="password"
          />
        </div>
        <div className={styles.btns}>
          <Button 
            disabled={!isValid}
            btnType='purple' 
            size='lg' 
            onClick={handleSubmit((data, evt) => onSubmit(data, evt, 'login'))}
            squared={true}
            type='submit'
            id={styles.login_btn}
          >Войти</Button>
          <Button 
            disabled={!isValid} 
            size='lg' 
            squared={true}
            onClick={handleSubmit((data, evt) => onSubmit(data, evt, 'registr'))}
            id={styles.register_btn}
          >Зарегистрироваться</Button>
        </div>
      </form>
    </div>
  );
};

export default AuthPage;