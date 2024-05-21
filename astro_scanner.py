import filtros

class AstroScanner:
    def analyze(self, traffic_data):
        # Analisa o tráfego em busca de bioassinaturas e technoassinaturas
        bio_signatures = filtros.detect_bio_signatures(traffic_data)
        tech_signatures = filtros.detect_tech_signatures(traffic_data)

        # Combina os resultados e gera um sinal de 0 a 100
        signal = 0
        if bio_signatures:
            signal += 50
        if tech_signatures:
            signal += 50

        # Retorna os resultados da análise
        return {
            "bio_signatures": bio_signatures,
            "tech_signatures": tech_signatures,
            "signal": signal
        }