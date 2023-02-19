import SourceCard from '../../components/SourceBadge/SourceBadge';
import { useGetAllSourcesQuery } from '../../services/apiService/apiService';
import styles from './SourcesPage.module.scss';

const sources = [
  {uuid: '1', name: 'Вышка', status: 'ok', rating: 4.92},
  {uuid: '2', name: 'МГТУ Баумана', status: 'critical', rating: 4.78},
  {uuid: '3', name: 'МФТИ', status: 'partial', rating: 4.95},
  {uuid: '4', name: 'Вышка', status: 'ok', rating: 4.92},
  {uuid: '5', name: 'МГТУ Баумана', status: 'critical', rating: 4.78},
  {uuid: '6', name: 'МФТИ', status: 'partial', rating: 4.95},
  {uuid: '7', name: 'Вышка', status: 'ok', rating: 4.92},
  {uuid: '8', name: 'МГТУ Баумана', status: 'critical', rating: 4.78},
  {uuid: '9', name: 'МФТИ', status: 'partial', rating: 4.95},
  {uuid: '10', name: 'МФТИ', status: 'partial', rating: 4.95},
]

const SourcesPage = () => {
  const {data: sources, isLoading} = useGetAllSourcesQuery()

  if (isLoading) {
    return null
  }

  // getAllSources().then(data => console.log(data))
  

  return (
    <div className={styles.container}>
      <h1 className='page_title'>Все ресурсы</h1>
      {sources?.length ?
        <div className={styles.table}>
          {sources.map((source, i) => <SourceCard i={i} key={source.uuid} {...source}/>)}
        </div>
        : <span className={styles.no_resources}>В базе данных пока нет ресурсов</span>
      }
    </div>
  );
};

export default SourcesPage;