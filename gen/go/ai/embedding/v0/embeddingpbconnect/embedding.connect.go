// Code generated by protoc-gen-connect-go. DO NOT EDIT.
//
// Source: ai/embedding/v0/embedding.proto

// buf:lint:ignore PACKAGE_VERSION_SUFFIX
package embeddingpbconnect

import (
	connect "connectrpc.com/connect"
	context "context"
	errors "errors"
	v0 "github.com/peak6-sites/r2g2-apis/gen/go/ai/embedding/v0"
	http "net/http"
	strings "strings"
)

// This is a compile-time assertion to ensure that this generated file and the connect package are
// compatible. If you get a compiler error that this constant is not defined, this code was
// generated with a version of connect newer than the one compiled into your binary. You can fix the
// problem by either regenerating this code with an older version of connect or updating the connect
// version compiled into your binary.
const _ = connect.IsAtLeastVersion1_13_0

const (
	// EmbeddingsName is the fully-qualified name of the Embeddings service.
	EmbeddingsName = "ai.embedding.v0.Embeddings"
)

// These constants are the fully-qualified names of the RPCs defined in this package. They're
// exposed at runtime as Spec.Procedure and as the final two segments of the HTTP route.
//
// Note that these are different from the fully-qualified method names used by
// google.golang.org/protobuf/reflect/protoreflect. To convert from these constants to
// reflection-formatted method names, remove the leading slash and convert the remaining slash to a
// period.
const (
	// EmbeddingsCreateEmbeddingProcedure is the fully-qualified name of the Embeddings's
	// CreateEmbedding RPC.
	EmbeddingsCreateEmbeddingProcedure = "/ai.embedding.v0.Embeddings/CreateEmbedding"
	// EmbeddingsComputeSimilarityProcedure is the fully-qualified name of the Embeddings's
	// ComputeSimilarity RPC.
	EmbeddingsComputeSimilarityProcedure = "/ai.embedding.v0.Embeddings/ComputeSimilarity"
	// EmbeddingsListModelsProcedure is the fully-qualified name of the Embeddings's ListModels RPC.
	EmbeddingsListModelsProcedure = "/ai.embedding.v0.Embeddings/ListModels"
)

// These variables are the protoreflect.Descriptor objects for the RPCs defined in this package.
var (
	embeddingsServiceDescriptor                 = v0.File_ai_embedding_v0_embedding_proto.Services().ByName("Embeddings")
	embeddingsCreateEmbeddingMethodDescriptor   = embeddingsServiceDescriptor.Methods().ByName("CreateEmbedding")
	embeddingsComputeSimilarityMethodDescriptor = embeddingsServiceDescriptor.Methods().ByName("ComputeSimilarity")
	embeddingsListModelsMethodDescriptor        = embeddingsServiceDescriptor.Methods().ByName("ListModels")
)

// EmbeddingsClient is a client for the ai.embedding.v0.Embeddings service.
type EmbeddingsClient interface {
	// Generates an embedding vector for the provided text using the specified model.
	CreateEmbedding(context.Context, *connect.Request[v0.CreateEmbeddingRequest]) (*connect.Response[v0.CreateEmbeddingResponse], error)
	// Calculates the similarity score between two texts using the specified model.
	ComputeSimilarity(context.Context, *connect.Request[v0.ComputeSimilarityRequest]) (*connect.Response[v0.ComputeSimilarityResponse], error)
	// Retrieves a list of available embedding models.
	ListModels(context.Context, *connect.Request[v0.ListModelsRequest]) (*connect.Response[v0.ListModelsResponse], error)
}

// NewEmbeddingsClient constructs a client for the ai.embedding.v0.Embeddings service. By default,
// it uses the Connect protocol with the binary Protobuf Codec, asks for gzipped responses, and
// sends uncompressed requests. To use the gRPC or gRPC-Web protocols, supply the connect.WithGRPC()
// or connect.WithGRPCWeb() options.
//
// The URL supplied here should be the base URL for the Connect or gRPC server (for example,
// http://api.acme.com or https://acme.com/grpc).
func NewEmbeddingsClient(httpClient connect.HTTPClient, baseURL string, opts ...connect.ClientOption) EmbeddingsClient {
	baseURL = strings.TrimRight(baseURL, "/")
	return &embeddingsClient{
		createEmbedding: connect.NewClient[v0.CreateEmbeddingRequest, v0.CreateEmbeddingResponse](
			httpClient,
			baseURL+EmbeddingsCreateEmbeddingProcedure,
			connect.WithSchema(embeddingsCreateEmbeddingMethodDescriptor),
			connect.WithClientOptions(opts...),
		),
		computeSimilarity: connect.NewClient[v0.ComputeSimilarityRequest, v0.ComputeSimilarityResponse](
			httpClient,
			baseURL+EmbeddingsComputeSimilarityProcedure,
			connect.WithSchema(embeddingsComputeSimilarityMethodDescriptor),
			connect.WithClientOptions(opts...),
		),
		listModels: connect.NewClient[v0.ListModelsRequest, v0.ListModelsResponse](
			httpClient,
			baseURL+EmbeddingsListModelsProcedure,
			connect.WithSchema(embeddingsListModelsMethodDescriptor),
			connect.WithClientOptions(opts...),
		),
	}
}

// embeddingsClient implements EmbeddingsClient.
type embeddingsClient struct {
	createEmbedding   *connect.Client[v0.CreateEmbeddingRequest, v0.CreateEmbeddingResponse]
	computeSimilarity *connect.Client[v0.ComputeSimilarityRequest, v0.ComputeSimilarityResponse]
	listModels        *connect.Client[v0.ListModelsRequest, v0.ListModelsResponse]
}

// CreateEmbedding calls ai.embedding.v0.Embeddings.CreateEmbedding.
func (c *embeddingsClient) CreateEmbedding(ctx context.Context, req *connect.Request[v0.CreateEmbeddingRequest]) (*connect.Response[v0.CreateEmbeddingResponse], error) {
	return c.createEmbedding.CallUnary(ctx, req)
}

// ComputeSimilarity calls ai.embedding.v0.Embeddings.ComputeSimilarity.
func (c *embeddingsClient) ComputeSimilarity(ctx context.Context, req *connect.Request[v0.ComputeSimilarityRequest]) (*connect.Response[v0.ComputeSimilarityResponse], error) {
	return c.computeSimilarity.CallUnary(ctx, req)
}

// ListModels calls ai.embedding.v0.Embeddings.ListModels.
func (c *embeddingsClient) ListModels(ctx context.Context, req *connect.Request[v0.ListModelsRequest]) (*connect.Response[v0.ListModelsResponse], error) {
	return c.listModels.CallUnary(ctx, req)
}

// EmbeddingsHandler is an implementation of the ai.embedding.v0.Embeddings service.
type EmbeddingsHandler interface {
	// Generates an embedding vector for the provided text using the specified model.
	CreateEmbedding(context.Context, *connect.Request[v0.CreateEmbeddingRequest]) (*connect.Response[v0.CreateEmbeddingResponse], error)
	// Calculates the similarity score between two texts using the specified model.
	ComputeSimilarity(context.Context, *connect.Request[v0.ComputeSimilarityRequest]) (*connect.Response[v0.ComputeSimilarityResponse], error)
	// Retrieves a list of available embedding models.
	ListModels(context.Context, *connect.Request[v0.ListModelsRequest]) (*connect.Response[v0.ListModelsResponse], error)
}

// NewEmbeddingsHandler builds an HTTP handler from the service implementation. It returns the path
// on which to mount the handler and the handler itself.
//
// By default, handlers support the Connect, gRPC, and gRPC-Web protocols with the binary Protobuf
// and JSON codecs. They also support gzip compression.
func NewEmbeddingsHandler(svc EmbeddingsHandler, opts ...connect.HandlerOption) (string, http.Handler) {
	embeddingsCreateEmbeddingHandler := connect.NewUnaryHandler(
		EmbeddingsCreateEmbeddingProcedure,
		svc.CreateEmbedding,
		connect.WithSchema(embeddingsCreateEmbeddingMethodDescriptor),
		connect.WithHandlerOptions(opts...),
	)
	embeddingsComputeSimilarityHandler := connect.NewUnaryHandler(
		EmbeddingsComputeSimilarityProcedure,
		svc.ComputeSimilarity,
		connect.WithSchema(embeddingsComputeSimilarityMethodDescriptor),
		connect.WithHandlerOptions(opts...),
	)
	embeddingsListModelsHandler := connect.NewUnaryHandler(
		EmbeddingsListModelsProcedure,
		svc.ListModels,
		connect.WithSchema(embeddingsListModelsMethodDescriptor),
		connect.WithHandlerOptions(opts...),
	)
	return "/ai.embedding.v0.Embeddings/", http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		switch r.URL.Path {
		case EmbeddingsCreateEmbeddingProcedure:
			embeddingsCreateEmbeddingHandler.ServeHTTP(w, r)
		case EmbeddingsComputeSimilarityProcedure:
			embeddingsComputeSimilarityHandler.ServeHTTP(w, r)
		case EmbeddingsListModelsProcedure:
			embeddingsListModelsHandler.ServeHTTP(w, r)
		default:
			http.NotFound(w, r)
		}
	})
}

// UnimplementedEmbeddingsHandler returns CodeUnimplemented from all methods.
type UnimplementedEmbeddingsHandler struct{}

func (UnimplementedEmbeddingsHandler) CreateEmbedding(context.Context, *connect.Request[v0.CreateEmbeddingRequest]) (*connect.Response[v0.CreateEmbeddingResponse], error) {
	return nil, connect.NewError(connect.CodeUnimplemented, errors.New("ai.embedding.v0.Embeddings.CreateEmbedding is not implemented"))
}

func (UnimplementedEmbeddingsHandler) ComputeSimilarity(context.Context, *connect.Request[v0.ComputeSimilarityRequest]) (*connect.Response[v0.ComputeSimilarityResponse], error) {
	return nil, connect.NewError(connect.CodeUnimplemented, errors.New("ai.embedding.v0.Embeddings.ComputeSimilarity is not implemented"))
}

func (UnimplementedEmbeddingsHandler) ListModels(context.Context, *connect.Request[v0.ListModelsRequest]) (*connect.Response[v0.ListModelsResponse], error) {
	return nil, connect.NewError(connect.CodeUnimplemented, errors.New("ai.embedding.v0.Embeddings.ListModels is not implemented"))
}
