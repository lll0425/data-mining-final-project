import pandas as pd
import sys

if __name__ == "__main__":
	if len(sys.argv) == 2:
		path_name = str(sys.argv[1])
		df = pd.read_csv(path_name)
		ari_mean = df['ari'].mean()
		nmi_mean = df['nmi'].mean()
		time_mean = df['ex_time'].mean()
		data = df['data'][0]
		alg = 'avg'
		n_c = df['n_c'][0]
		print('data: ',data)
		print('ari_mean: ',ari_mean)
		print('nmi_mean: ',nmi_mean)
		print('time_mean: ',time_mean)
		df.loc[len(df)] = [alg, data, ari_mean, nmi_mean,n_c ,time_mean]
		df.to_csv(path_name, index=False)  