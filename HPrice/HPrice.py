import pandas as pd

class HPrice:
    #inpot data for making an instance is a pandas dataframe with columns:date, open, high,low,clos,volume,
    # and n represents number of candles colliding to two price, one high and one low
    def __init__(self, data, n):
        self.data = data
        self.n = n

    def HPrice(self):
        date = []
        price = []
        volume = []

        for i in range(self.data.shape[0] % self.n, self.data.shape[0], self.n):
            sub_df = self.data[i: i+self.n]
            max_index = sub_df['high'].idxmax()
            min_index = sub_df['low'].idxmin()
            if max_index < min_index:
                date.append(sub_df['date'][max_index])
                date.append(sub_df['date'][min_index])

                price.append(sub_df['high'][max_index])
                price.append(sub_df['low'][min_index])

                volume.append(sub_df['volume'][max_index])
                volume.append(sub_df['volume'][min_index])

            elif max_index > min_index:
                date.append(sub_df['date'][min_index])
                date.append(sub_df['date'][max_index])

                price.append(sub_df['low'][min_index])
                price.append(sub_df['high'][max_index])

                volume.append(sub_df['volume'][min_index])
                volume.append(sub_df['volume'][max_index])

            else:
                if sub_df['close'][max_index] > sub_df['open'][max_index]:
                    date.append(sub_df['date'][min_index])
                    date.append(sub_df['date'][max_index])

                    price.append(sub_df['low'][min_index])
                    price.append(sub_df['high'][max_index])

                    volume.append(sub_df['volume'][min_index])
                    volume.append(sub_df['volume'][max_index])

                else:
                    date.append(sub_df['date'][max_index])
                    date.append(sub_df['date'][min_index])

                    price.append(sub_df['high'][max_index])
                    price.append(sub_df['low'][min_index])

                    volume.append(sub_df['volume'][max_index])
                    volume.append(sub_df['volume'][min_index])


            result = pd.DataFrame(list(zip(date, price, volume)), columns=['date', 'price', 'volume'])
        return result