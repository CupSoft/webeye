import SourceCard from '../../components/SourceCard/SourceCard';
import styles from './SourcesPage.module.scss';

const sources = [
  {id: 1, name: 'Вышка', state: 'Normal', rating: 4.92},
  {id: 2, name: 'МГТУ Баумана', state: 'Critical', rating: 4.78},
  {id: 3, name: 'МФТИ', state: 'Partial', rating: 4.95},
]

const SourcesPage = () => {
  return (
    <div className={styles.container}>
      <h1 className='page_title'>Все ресурсы</h1>
      <div className={styles.table}>
        {sources.map((source, i) => <SourceCard i={i} key={source.id} {...source}/>)}
      </div>
    </div>
  );
};

export default SourcesPage;