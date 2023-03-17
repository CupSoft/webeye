import { FieldValues, useForm } from 'react-hook-form';
import { toast } from 'react-toastify';
import { useAdminPostResourceMutation, useAdminPostResourceNodeMutation } from '../../../services/apiService/apiService';
import { AdminPostResourceRequestTypes } from '../../../services/apiService/apiServiceTypes';
import Button from '../../UI/Button/Button';
import Input from '../../UI/Input/Input';

const CreateResourceForm = () => {
  const {
    register,
    handleSubmit,
    reset,
    formState: {errors, isDirty, isValid}
  } = useForm({mode: 'onBlur'})
  const [adminPostResource] = useAdminPostResourceMutation()
  const [adminPostResourceNode] = useAdminPostResourceNodeMutation()

  function onSubmit(data: FieldValues) {
    adminPostResource(data as AdminPostResourceRequestTypes).then(value => {
      if ('error' in value) {
        toast('Ресурс с таким именем уже сществует')
        return
      }

      adminPostResourceNode({ 
        url: data.url, 
        resource_uuid: value.data.uuid
      }).then(value1 => {
        if ('error' in value1) {
          toast('Ошибка при создании первичной ноды')
          return
        }

        reset()
        toast('Ресурс успешно добавлен в базу данных')
      })
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
        <Input
          placeholder='Введите URL ресурса...'
          register={register} 
          name='url'
          options={{
            minLength: 1,
            required: true,
          }}
        />
        <Button
          size='md'
          btnType='purple'
          disabled={!isValid}
        >Добавить ресурс</Button>
      </div>
    </form>
  );
};

export default CreateResourceForm;