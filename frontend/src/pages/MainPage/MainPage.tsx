import Card from '../../components/Card/Card';
import styles from './MainPage.module.scss'

const MainPage = () => {
  return (
    <div className={styles.container}>
      <h1 className='page_title'>Мониторинг система</h1>
      <span className={styles.description}>Наша система отслеживает состояние и доступность информационных ресурсов российских ВУЗов</span>
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
          description='Любую статистику на этом сайте вы можете свободно скачать в разных форматах'
          size='sm'
        />
        <Card
          icon='sources'  
          title='Источники'
          description='Наша система производит мониторинг ресурсов из разных источников, таких как социальные сети, множество серверов в разных странах и городах и сообщения от сообщества'
          size='sm'
        />
      </div>
    </div>
  );
};

export default MainPage;