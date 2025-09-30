

# Criar o diagrama DER
dot = digraph(comment="DER - Diagrama Entidade Relacionamento", format="png")
dot.attr(rankdir="LR", size="8")

# Entidades
dot.node("Usuario", "Usuário\nid_usuario (PK)\nemail\nsenha", shape="record")
dot.node("Perfil", "Perfil\nid_perfil (PK)\nnome\nendereco\ntelefone\ndata_nascimento", shape="record")
dot.node("Compra", "Compra\nid_compra (PK)\nnum_compra\nvalor_compra", shape="record")
dot.node("Produto", "Produto\nid_produto (PK)\nitem\nvalor_unit\ndata_validade\ndescricao", shape="record")
dot.node("CompraProdutos", "Compra_Produtos\nid_compra_prod (PK)\nid_compra (FK)\nid_produto (FK)\nquantidade", shape="record")

# Relacionamentos
dot.edge("Usuario", "Perfil", label="1:1")
dot.edge("Usuario", "Compra", label="1:N")
dot.edge("Compra", "CompraProdutos", label="1:N")
dot.edge("Produto", "CompraProdutos", label="1:N")

# Renderizar
output_path = "/mnt/data/DER_diagrama"
dot.render(output_path, format="png", cleanup=True)
output_path + ".png"