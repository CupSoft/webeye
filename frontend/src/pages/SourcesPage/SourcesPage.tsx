import SourcesTable from '../../components/SourcesTable/SourcesTable';
import styles from './SourcesPage.module.scss';

const SourcesPage = () => {

  return (
    <div className={styles.container}>
      <h1 className='page_title'>Все ресурсы</h1>
      <SourcesTable />
    </div>
  );
};

export default SourcesPage;