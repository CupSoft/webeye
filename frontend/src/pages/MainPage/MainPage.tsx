import Card from '../../components/Card/Card';
import styles from './MainPage.module.scss'

const MainPage = () => {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Мониторинг система</h1>
      <span className={styles.description}>Наша система отслеживает состояние и доступность информационных ресурсов российских ВУЗов</span>
      <div className={styles.cards}>
        <Card
          icon='community'
          title='Сообщество'
          size='sm'
        >
          Сообщайте о недоступности ресурсов и оставляйте отзывы, пополняя общую базу данных
        </Card>
        <Card
          icon='handshake'
          title='Экспорт'
          size='sm'
        >
          Любую статистику на этом сайте вы можете свободно скачать в разных форматах
        </Card>
        <Card
          icon='sources'  
          title='Источники'
          size='sm'
        >
          Наша система производит мониторинг ресурсов из разных источников, таких как социальные сети, множество серверов в разных странах и городах и сообщения от сообщества
        </Card>
      </div>
    </div>
  );
};

export default MainPage;