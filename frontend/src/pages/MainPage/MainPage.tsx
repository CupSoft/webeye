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
          description='Вы можете бесплатно получить любую статистику на этом сайте'
          size='sm'
        />
        <Card
          icon='sources'  
          title='Источники'
          description='Наша система производит мониторинг ресурсов из разных источников: посредством социальных сетей и серверов в разных городах, а также учитываются сообщения от пользователей'
          size='sm'
        />
      </div>
    </div>
  );
};

export default MainPage;