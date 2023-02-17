import { FieldValues, useForm } from 'react-hook-form';
import { useNavigate, useSearchParams } from 'react-router-dom';
import { useAppDispatch } from '../../app/hooks';
import Button from '../../components/UI/Button/Button';
import Input from '../../components/UI/Input/Input';
import { emailPattern, MAIN_ROUTE, SOURCES_ROUTE } from '../../utils/constants';
import styles from './AuthPage.module.scss';

const AuthPage = () => {
  const {
    register,
    handleSubmit,
    formState: {errors, isDirty, isValid}
  } = useForm({mode: 'onBlur'})
  const dispatch = useAppDispatch()
  const navigate = useNavigate()
  const params = new URLSearchParams(window.location.search)

  function onSubmit(data: FieldValues) {
    dispatch({type: 'auth', payload: true})
    navigate(params.get('next_page') ?? MAIN_ROUTE)
  }

  return (
    <div className={styles.container}>
      <form 
        className={styles.form}
        onSubmit={handleSubmit(onSubmit)}
      >
        <div className={styles.inputs}>
          <Input
            // maxLength={10}
            options={{
              minLength: 1,
              required: true,
              pattern: emailPattern
            }}
            register={register}
            placeholder="E-mail..."
            name="email"
          />
          <Input
            // maxLength={10}
            options={{
              minLength: 1,
              required: true
            }}
            register={register}
            placeholder="Password..."
            name="password"
          />
        </div>
        <div className={styles.btns}>
          <Button 
            disabled={!isValid} 
            size='lg' 
            squared={true}
            id={styles.register_btn}
          >Зарегистрироваться</Button>
          <Button 
            disabled={!isValid}
            btnType='purple' 
            size='lg' 
            squared={true}
            id={styles.login_btn}
          >Войти</Button>
        </div>
      </form>
    </div>
  );
};

export default AuthPage;