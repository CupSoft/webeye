import { useEffect, useState } from 'react';
import { toast } from 'react-toastify';
import { useAdminDeleteResourceMutation, useGetAllSourcesQuery } from '../../../services/apiService/apiService';
import { SourceGetTypes } from '../../../services/apiService/apiServiceTypes';
import SourceCard from '../../SourceBadge/SourceBadge';
import Button from '../../UI/Button/Button';
import styles from './DeleteResourceForm.module.scss';

const DeleteResourceForm = () => {
  const {data, isLoading} = useGetAllSourcesQuery({})
  const [adminDeleteResource] = useAdminDeleteResourceMutation()
  const [sources, setSources] = useState<SourceGetTypes[]>([])

  useEffect(() => {
    if (data) {
      setSources(data)
    }
  }, [data])

  if (isLoading) {
    return null
  }

  function deleteClickHandler(uuid: string) {
    adminDeleteResource(uuid).then(value => {
      if ('error' in value) {
        toast('Не получилось удалить ресурс')
        return
      }
      setSources(sources.filter((source) => source.uuid !== uuid))
      toast('Ресурс успешно удален')
    })
  }

  return (
    <div className='admin_container'>
      <div className='admin_wrapper'>
        <h3 className='admin_title'>Существующие ресурсы</h3>
        {sources?.length ?
        <div className={styles.table}>
          {sources.map((source, i) => 
            <div className={styles.wrapper} key={source.uuid}>
              <SourceCard i={i} {...source}/>
              <Button 
                noWrap={true}
                btnType={'red'}
                myClass={styles.delete_btn}
                onClick={() => deleteClickHandler(source.uuid)}
              ><span></span></Button>
            </div>
          )}
        </div>
        : <span className={styles.no_resources}>В базе данных пока нет ресурсов</span>
      }
      </div>
    </div>
  );
};

export default DeleteResourceForm;