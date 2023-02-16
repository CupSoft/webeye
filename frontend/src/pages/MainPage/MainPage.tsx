import styles from './MainPage.module.scss'

const MainPage = () => {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Мониторинг система</h1>
      <span className={styles.description}>Наша система отслеживает состояние и доступность информационных ресурсов российских ВУЗов</span>
    </div>
  );
};

export default MainPage;