import Card from '../../components/Card/Card';
import SourcesTable from '../../components/SourcesTable/SourcesTable';
import styles from './MainPage.module.scss'
import {useEffect, useState,} from 'react'
import { useGetDdosMutation } from '../../services/apiService/apiService';

const MainPage = () => {
  const [isDdos, setIsDdos] = useState(false)
  const [getDdos] = useGetDdosMutation()

  useEffect(() => {
    getDdos().then(value => {
      if ('error' in value) {
        return
      }

      setIsDdos(value.data.is_ddos)
    })
  }, [])

  return (
    <div className={styles.container}>
      {isDdos && <span className={styles.ddos}>Зафиксирована массовая атака</span>}
      <h1 className='page_title'>Мониторинг система</h1>
      <span className={styles.description}>Наша система отслеживает состояние и доступность информационных ресурсов российских ВУЗов</span>
      <SourcesTable limit={10}/>
      <div className={styles.cards}>
        <Card
          icon='community'
          title='Сообщество'
          description='Сообщайте о недоступности ресурсов и оставляйте отзывы, пополняя общую базу данных'
          size='sm'
        />
        <Card
          icon='handshake'
          title='Экспорт'
          description='Вы можете бесплатно получить любую статистику на этом сайте'
          size='sm'
        />
        <Card
          icon='sources'  
          title='Источники'
          description='Система производит мониторинг ресурсов из разных источников: соц-сетей, наших серверов в разных городах и сообщений от сообщества'
          size='sm'
        />
      </div>
    </div>
  );
};

export default MainPage;