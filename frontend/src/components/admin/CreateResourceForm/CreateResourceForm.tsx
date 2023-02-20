import React from 'react';
import { FieldValues, useForm } from 'react-hook-form';
import { toast } from 'react-toastify';
import { useAdminPostResourceMutation } from '../../../services/apiService/apiService';
import { AdminPostResourceTypes } from '../../../services/apiService/apiServiceTypes';
import Button from '../../UI/Button/Button';
import Input from '../../UI/Input/Input';
import styles from './CreateResourceForm.module.scss'

const CreateResourceForm = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: {errors, isDirty, isValid}
  } = useForm({mode: 'onBlur'})
  const [adminPostResource] = useAdminPostResourceMutation()

  function onSubmit(data: FieldValues) {
    adminPostResource(data as AdminPostResourceTypes).then(value => {
      if ('error' in value) {
        toast('Ресурс с таким именем уже сществует')
        return
      }

      reset()
      toast('Ресурс успешно добавлен в базу данных')
    })
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)} className='admin_container'>
      <div className='admin_wrapper'>
        <h3 className='admin_title'>Добавление ресурса</h3>
        <Input
          placeholder='Введите имя ресурса...'
          register={register} 
          name='name'
          options={{
            minLength: 1,
            required: true,
          }}
        />
        <Button
          size='md'
          disabled={!isValid}
        >Добавить ресурс</Button>
      </div>
    </form>
  );
};

export default CreateResourceForm;