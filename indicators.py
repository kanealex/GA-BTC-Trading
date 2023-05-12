from ta.volatility import BollingerBands
from ta.volatility import AverageTrueRange
from ta.volatility import KeltnerChannel
from ta.volatility import DonchianChannel
from ta.momentum import RSIIndicator
from ta.momentum import StochasticOscillator
from ta.momentum import ROCIndicator
from ta.momentum import AwesomeOscillatorIndicator
from ta.momentum import KAMAIndicator
from ta.momentum import PercentagePriceOscillator
from ta.trend import SMAIndicator, MACD
from ta.trend import EMAIndicator
from ta.trend import PSARIndicator
from ta.trend import CCIIndicator
from ta.trend import ADXIndicator
from ta.trend import AroonIndicator
from ta.trend import DPOIndicator
from ta.trend import KSTIndicator
from ta.trend import MassIndex
from ta.trend import STCIndicator
from ta.trend import TRIXIndicator
from ta.trend import VortexIndicator
from ta.trend import WMAIndicator
from ta.volume import OnBalanceVolumeIndicator
from ta.volume import MFIIndicator

def awesome_oscillator(data, window1=5, window2=34):
    ao_string = f"ao_{window1}_{window2}"
    if ao_string in data.columns:
        return ao_string
    ao_indicator = AwesomeOscillatorIndicator(data['h'], data['l'], window1=window1, window2=window2)
    ao_value = ao_indicator.awesome_oscillator()
    data[ao_string] = ao_value
    return ao_string

def kama(data, window=10, pow1=2, pow2=30):
    kama_string = f"kama_{window}_{pow1}_{pow2}"
    if kama_string in data.columns:
        return kama_string
    kama_indicator = KAMAIndicator(data['c'], window=window, pow1=pow1, pow2=pow2)
    kama_value = kama_indicator.kama()
    data[kama_string] = kama_value
    return kama_string

def ppo_line(data, window_slow=26, window_fast=12, window_sign=9):
    ppo_line_string = f"ppo_line_{window_slow}_{window_fast}"
    if ppo_line_string in data.columns:
        return ppo_line_string
    ppo_indicator = PercentagePriceOscillator(data['c'], window_slow=window_slow, window_fast=window_fast)
    ppo_line_value = ppo_indicator.ppo()
    data[ppo_line_string] = ppo_line_value
    return ppo_line_string

def ppo_signal(data, window_slow=26, window_fast=12, window_sign=9):
    ppo_signal_string = f"ppo_signal_{window_slow}_{window_fast}_{window_sign}"
    if ppo_signal_string in data.columns:
        return ppo_signal_string
    ppo_indicator = PercentagePriceOscillator(data['c'], window_slow=window_slow, window_fast=window_fast, window_sign=window_sign)
    ppo_signal_value = ppo_indicator.ppo_signal()
    data[ppo_signal_string] = ppo_signal_value
    return ppo_signal_string

def adx(data, adx_period=14):
    adx_string = f"adx_{adx_period}"
    if adx_string in data.columns:
        return adx_string
    adx_indicator = ADXIndicator(data['h'], data['l'], data['c'], window=adx_period)
    adx = adx_indicator.adx()
    data[adx_string] = adx
    return adx_string

def kc_upperband(data, kc_period=20):
    kc_string = f"kc_upperband_{kc_period}"
    if kc_string in data.columns:
        return kc_string
    kc_indicator = KeltnerChannel(data['h'], data['l'], data['c'], window=kc_period)
    kc_upperband = kc_indicator.keltner_channel_hband()
    data[kc_string] = kc_upperband
    return kc_string

def kc_lowerband(data, kc_period=20):
    kc_string = f"kc_lowerband_{kc_period}"
    if kc_string in data.columns:
        return kc_string
    kc_indicator = KeltnerChannel(data['h'], data['l'], data['c'], window=kc_period)
    kc_lowerband = kc_indicator.keltner_channel_lband()
    data[kc_string] = kc_lowerband
    return kc_string

def dc(data, dc_period=20):
    dc_string = f"dc_{dc_period}"
    if dc_string in data.columns:
        return dc_string
    dc_indicator = DonchianChannel(data['h'], data['l'], data['c'], window=dc_period)
    dc_upperband = dc_indicator.donchian_channel_hband()
    dc_lowerband = dc_indicator.donchian_channel_lband()
    data[dc_string] = (data['c'] - dc_lowerband) / (dc_upperband - dc_lowerband)
    return dc_string

def aroon_up(data, aroon_period=25):
    aroon_up_string = f"aroon_up_{aroon_period}"
    if aroon_up_string in data.columns:
        return aroon_up_string
    aroon_indicator = AroonIndicator(data['c'], window=aroon_period)
    aroon_up = aroon_indicator.aroon_up()
    data[aroon_up_string] = aroon_up
    return aroon_up_string

def aroon_down(data, aroon_period=25):
    aroon_down_string = f"aroon_down_{aroon_period}"
    if aroon_down_string in data.columns:
        return aroon_down_string
    aroon_indicator = AroonIndicator(data['c'], window=aroon_period)
    aroon_down = aroon_indicator.aroon_down()
    data[aroon_down_string] = aroon_down
    return aroon_down_string

def dpo(data, dpo_period=20):
    dpo_string = f"dpo_{dpo_period}"
    if dpo_string in data.columns:
        return dpo_string
    dpo_indicator = DPOIndicator(data['c'], window=dpo_period)
    dpo_value = dpo_indicator.dpo()
    data[dpo_string] = dpo_value
    return dpo_string

def kst(data, r1=10, r2=15, r3=20, r4=30, n1=10, n2=10, n3=10, n4=15):
    kst_string = f"kst_{r1}_{r2}_{r3}_{r4}_{n1}_{n2}_{n3}_{n4}"
    if kst_string in data.columns:
        return kst_string
    kst_indicator = KSTIndicator(data['c'], r1, r2, r3, r4, n1, n2, n3, n4)
    kst_value = kst_indicator.kst()
    data[kst_string] = kst_value
    return kst_string

def kst_signal(data, roc1=10, roc2=15, roc3=20, roc4=30, sma1=10, sma2=10, sma3=10, sma4=15, signal=9):
    kst_sig_string = f"kst_signal_{roc1}_{roc2}_{roc3}_{roc4}_{sma1}_{sma2}_{sma3}_{sma4}_{signal}"
    if kst_sig_string in data.columns:
        return kst_sig_string
    kst_indicator = KSTIndicator(data['c'], roc1, roc2, roc3, roc4, sma1, sma2, sma3, sma4, signal)
    kst_signal = kst_indicator.kst_sig()
    data[kst_sig_string] = kst_signal
    return kst_sig_string

def trix(data, trix_period=18):
    trix_string = f"trix_{trix_period}"
    if trix_string in data.columns:
        return trix_string
    trix_indicator = TRIXIndicator(data['c'], window=trix_period)
    trix = trix_indicator.trix()
    data[trix_string] = trix
    return trix_string

def vortex_pos(data, vortex_period=14):
    vortex_pos_string = f"vortex_pos_{vortex_period}"
    if vortex_pos_string in data.columns:
        return vortex_pos_string
    vortex_indicator = VortexIndicator(data['h'], data['l'], data['c'], window=vortex_period)
    vortex_pos = vortex_indicator.vortex_indicator_pos()
    data[vortex_pos_string] = vortex_pos
    return vortex_pos_string

def vortex_neg(data, vortex_period=14):
    vortex_neg_string = f"vortex_neg_{vortex_period}"
    if vortex_neg_string in data.columns:
        return vortex_neg_string
    vortex_indicator = VortexIndicator(data['h'], data['l'], data['c'], window=vortex_period)
    vortex_neg = vortex_indicator.vortex_indicator_neg()
    data[vortex_neg_string] = vortex_neg
    return vortex_neg_string

def wma(data, wma_period=20):
    wma_string = f"wma_{wma_period}"
    if wma_string in data.columns:
        return wma_string
    wma_indicator = WMAIndicator(data['c'], window=wma_period)
    wma = wma_indicator.wma()
    data[wma_string] = wma
    return wma_string

def mass(data, window_fast=9, window_slow=25):
    mass_string = f"mass_{window_fast}_{window_slow}"
    if mass_string in data.columns:
        return mass_string
    mass_indicator = MassIndex(data['h'], data['l'], window_fast=window_fast, window_slow=window_slow)
    mass_value = mass_indicator.mass_index()
    data[mass_string] = mass_value
    return mass_string

def stc(data, window_fast=23, window_slow=50, cycle=10, smooth1=3, smooth2=3):
    stc_string = f"stc_{window_fast}_{window_slow}_{cycle}_{smooth1}_{smooth2}"
    if stc_string in data.columns:
        return stc_string
    stc_indicator = STCIndicator(data['c'], window_fast=window_fast, window_slow=window_slow, cycle=cycle, smooth1=smooth1, smooth2=smooth2)
    stc_value = stc_indicator.stc()
    data[stc_string] = stc_value
    return stc_string

def ema(data, ema_period=20):
    ema_string = f"ema_{ema_period}"
    if ema_string in data.columns:
        return ema_string
    ema_indicator = EMAIndicator(data['c'], window=ema_period)
    ema = ema_indicator.ema_indicator()
    data[ema_string] = ema
    return ema_string

def psar(data, step=0.02, max_step=0.2):
    psar_string = f"psar_{step}_{max_step}".replace('.', '_')
    if psar_string in data.columns:
        return psar_string
    psar_indicator = PSARIndicator(data['h'], data['l'], data['c'], step=step, max_step=max_step)
    psar = psar_indicator.psar()
    data[psar_string] = psar
    return psar_string

def obv(data):
    obv_string = "obv"
    if obv_string in data.columns:
        return obv_string
    obv_indicator = OnBalanceVolumeIndicator(data['c'], data['v'])
    obv = obv_indicator.on_balance_volume()
    data[obv_string] = obv
    return obv_string

def mfi(data, mfi_period=14):
    mfi_string = f"mfi_{mfi_period}"
    if mfi_string in data.columns:
        return mfi_string
    mfi_indicator = MFIIndicator(data['h'], data['l'], data['c'], data['v'], window=mfi_period)
    mfi = mfi_indicator.money_flow_index()
    data[mfi_string] = mfi
    return mfi_string

def roc(data, roc_period=12):
    roc_string = f"roc_{roc_period}"
    if roc_string in data.columns:
        return roc_string
    roc_indicator = ROCIndicator(data['c'], window=roc_period)
    roc = roc_indicator.roc()
    data[roc_string] = roc
    return roc_string

def bollinger_bands_upper(data, bollinger_period=20, bollinger_std_dev=2):
    bollinger_string = f"bollinger_upper_{bollinger_period}_{bollinger_std_dev:.2f}".replace('.', '_')
    if bollinger_string in data.columns:
        return bollinger_string
    bollinger_indicator = BollingerBands(data['c'], window=bollinger_period, window_dev=bollinger_std_dev)
    data[bollinger_string] = bollinger_indicator.bollinger_hband()
    return bollinger_string

def bollinger_bands_lower(data, bollinger_period=20, bollinger_std_dev=2):
    bollinger_string = f"bollinger_lower_{bollinger_period}_{bollinger_std_dev:.2f}".replace('.', '_')
    if bollinger_string in data.columns:
        return bollinger_string
    bollinger_indicator = BollingerBands(data['c'], window=bollinger_period, window_dev=bollinger_std_dev)
    data[bollinger_string] = bollinger_indicator.bollinger_lband()
    return bollinger_string

def stochastic_oscillator_K(data, k_period=14, d_period=3):
    stoch_k_string = f"stochastic_K_{k_period}_{d_period}"
    if stoch_k_string in data.columns:
        return stoch_k_string
    stoch_indicator = StochasticOscillator(data['h'], data['l'], data['c'], k_period, d_period)
    data[stoch_k_string] = stoch_indicator.stoch()
    return stoch_k_string

def stochastic_oscillator_D(data, k_period=14, d_period=3):
    stoch_d_string = f"stochastic_D_{k_period}_{d_period}"
    if stoch_d_string in data.columns:
        return stoch_d_string
    stoch_indicator = StochasticOscillator(data['h'], data['l'], data['c'], k_period, d_period)
    data[stoch_d_string] = stoch_indicator.stoch_signal()
    return stoch_d_string

def atr(data, atr_period=14):
    atr_string = f"atr_{atr_period}"
    if atr_string in data.columns:
        return atr_string
    atr_indicator = AverageTrueRange(data['h'], data['l'], data['c'], window=atr_period)
    data[atr_string] = atr_indicator.average_true_range()
    return atr_string

def rsi(data, rsi_period = 14):
    rsi_string = f"rsi_{rsi_period}"
    if rsi_string in data.columns:
        return rsi_string
    rsi_indicator = RSIIndicator(data['c'], window=rsi_period)
    rsi = rsi_indicator.rsi()
    data[rsi_string] = rsi
    return rsi_string

def sma(data, sma_period=20):
    sma_string = f"sma_{sma_period}"
    if sma_string in data.columns:
        return sma_string
    sma_indicator = SMAIndicator(data['c'], window=sma_period)
    sma = sma_indicator.sma_indicator()
    data[sma_string] = sma
    return sma_string

def macd(data, macd_fast=12, macd_slow=26, macd_signal=9):
    macd_string = f"macd_{macd_fast}_{macd_slow}_{macd_signal}"
    if macd_string in data.columns:
        return macd_string
    macd_indicator = MACD(data['c'], macd_fast, macd_slow, macd_signal)
    macd = macd_indicator.macd()  # MACD line
    data[macd_string] = macd
    return macd_string

def macd_signal(data, macd_fast=12, macd_slow=26, macd_signal=9):
    macd_sig_string = f"macd_signal_{macd_fast}_{macd_slow}_{macd_signal}"
    if macd_sig_string in data.columns:
        return macd_sig_string
    macd_indicator = MACD(data['c'], macd_fast, macd_slow, macd_signal)
    macd_sig = macd_indicator.macd_signal()  # Signal line
    data[macd_sig_string] = macd_sig
    return macd_sig_string

def macd_histogram(data, macd_fast=12, macd_slow=26, macd_signal=9):
    macd_hist_string = f"macd_histogram_{macd_fast}_{macd_slow}_{macd_signal}"
    if macd_hist_string in data.columns:
        return macd_hist_string
    macd_indicator = MACD(data['c'], macd_fast, macd_slow, macd_signal)
    macd_hist = macd_indicator.macd_diff()  
    data[macd_hist_string] = macd_hist
    return macd_hist_string

def cci(data, cci_period=20):
    cci_string = f"cci_{cci_period}"
    if cci_string in data.columns:
        return cci_string
    cci_indicator = CCIIndicator(data['h'], data['l'], data['c'], window=cci_period)
    cci = cci_indicator.cci()
    data[cci_string] = cci
    return cci_string

def constant(data, constant=30):
    const_string = f"constant_{constant}".replace('.', '_')
    if const_string in data.columns:
        return const_string
    data[const_string] = constant
    return const_string

def candle(data,candle ="o"):
    return candle